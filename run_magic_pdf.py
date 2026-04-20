import subprocess
import os

def run_magic_pdf():
    output_dir = "./magic_pdf_output"
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Run magic-pdf command
        # Using -p for path, -o for output directory, -m for method (auto)
        cmd = [
            "magic-pdf", 
            "-p", "test.pdf", 
            "-o", output_dir, 
            "-m", "txt"
        ]
        
        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("magic-pdf executed successfully.")
        print("Output:", result.stdout)
        print("Stderr:", result.stderr)
        
    except subprocess.CalledProcessError as e:
        print(f"Error running magic-pdf: {e}")
        print("Stdout:", e.stdout)
        print("Stderr:", e.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_magic_pdf()
