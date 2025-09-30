import numpy as np
from torch_molecule import EdgePredMolecularEncoder

def test_edgepred_encoder():
    # Test molecules (simple examples)
    molecules = [
        "CC(=O)O",  # Acetic acid
        "CCO",      # Ethanol
        "CCCC",     # Butane
        "c1ccccc1", # Benzene
        "CCN",      # Ethylamine
    ]

    # Basic initilization test
    model = EdgePredMolecularEncoder(
        num_layer=3,
        hidden_size=300,
        batch_size=5,
        epochs=5,  # Small number for testing
        verbose="progress_bar"
    )
    print("Model initialized successfully")
    
    # Basic self-supervised fitting test
    print("\n=== Testing EdgePred model self-supervised fitting ===")
    model.fit(molecules[:4])
    
    # Model saving and loading test
    print("\n=== Testing model saving and loading ===")
    save_path = "test_model.pt"
    model.save_to_local(save_path)
    print(f"Model saved to {save_path}")

    new_model = EdgePredMolecularEncoder()
    new_model.load_from_local(save_path)
    print("Model loaded successfully")
    
    # Clean up
    import os
    if os.path.exists(save_path):
        os.remove(save_path)
        print(f"Cleaned up {save_path}")

if __name__ == "__main__":
    test_edgepred_encoder()