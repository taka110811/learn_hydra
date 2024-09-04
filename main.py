# main.py
import hydra

@hydra.main(config_path="conf", config_name="config", version_base="1.1")
def my_app(cfg):
    print("Hidden Size:", cfg.model.hidden_size)
    print("Learning rate:", cfg.model.learning_rate)
    print("Batch size:", cfg.model.batch_size)
    print("Number of epochs:", cfg.model.num_epochs)

if __name__ == "__main__":
    my_app()