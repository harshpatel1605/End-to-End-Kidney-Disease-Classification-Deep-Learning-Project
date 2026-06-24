import tensorflow as tf
import numpy as np
import math
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.utils.class_weight import compute_class_weight
from KidneyDiseaseClassification.entity.config_entity import TrainingConfig

class Training:
    def __init__(self,config:TrainingConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):

        datagenerator_kwargs = dict(
            validation_split = 0.20
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = 15,
                horizontal_flip = True,
                width_shift_range = 0.1,
                height_shift_range = 0.1,
                shear_range = 0.1,
                zoom_range = 0.1,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "training",
            shuffle = True,
            **dataflow_kwargs
        )

    def get_class_weights(self):
        labels = self.train_generator.classes
        weights = compute_class_weight(
            class_weight='balanced',
            classes=np.unique(labels),
            y=labels
        )
        return dict(enumerate(weights))

    def get_callbacks(self):
        return [
            tf.keras.callbacks.EarlyStopping(
                monitor = 'val_loss',
                patience = 5,
                restore_best_weights = True
            ),
            tf.keras.callbacks.ModelCheckpoint(
                filepath = str(self.config.trained_model_path),
                monitor = 'val_accuracy',
                save_best_only = True
            ),
            tf.keras.callbacks.ReduceLROnPlateau(
                monitor = 'val_loss',
                factor = 0.5,
                patience = 3,
                min_lr = 1e-7
            )
        ]
    
    def plot_training(self, history):
        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(history.history['accuracy'], label='Train Accuracy')
        ax.plot(history.history['val_accuracy'], label='Val Accuracy')
        ax.plot(history.history['loss'], label='Train Loss')
        ax.plot(history.history['val_loss'], label='Val Loss')

        ax.set_title('Training History')
        ax.set_xlabel('Epoch')
        ax.legend()

        plt.tight_layout()
        plt.savefig('training_plot.png')
        print("Plot saved as training_plot.png")

    def train(self):
        self.step_per_epochs = math.ceil(self.train_generator.samples / self.train_generator.batch_size)
        self.validation_step = math.ceil(self.valid_generator.samples / self.valid_generator.batch_size)

        history = self.model.fit(
            self.train_generator,
            epochs = self.config.params_epochs,
            steps_per_epoch = self.step_per_epochs,
            validation_steps = self.validation_step,
            validation_data = self.valid_generator,
            class_weight = self.get_class_weights(), 
            callbacks = self.get_callbacks()
        )

        self.plot_training(history=history)

        self.save_model(
            path=self.config.trained_model_path,
            model= self.model
        )

        self.save_model_for_github(self.model)
    
    @staticmethod
    def save_model_for_github(model: tf.keras.Model):
        save_dir = Path("model")
        save_dir.mkdir(parents=True, exist_ok=True)
        model.save(save_dir / "model.keras")

    @staticmethod
    def save_model(path:Path , model:tf.keras.Model):
        model.save(path)

