import os
import subprocess

# Dossiers
SRC_DIR = "src"
BUILD_DIR = "build"
EXEC_NAME = "openmc"  # Nom de l'exécutable final

# Options de compilation
LIBS = ["-lglfw", "-lGL", "-lX11", "-lpthread", "-lXrandr", "-lXi", "-ldl"]

def main():
    # Vérifie si le dossier build existe, sinon le créer
    os.makedirs(BUILD_DIR, exist_ok=True)

    # Liste tous les fichiers C dans src
    c_files = [os.path.join(SRC_DIR, f) for f in os.listdir(SRC_DIR) if f.endswith(".c")]

    if not c_files:
        print("Aucun fichier .c trouvé dans", SRC_DIR)
        return

    # Fichier exécutable de sortie
    output_path = os.path.join(BUILD_DIR, EXEC_NAME)

    # Commande de compilation
    cmd = ["gcc", "-o", output_path] + c_files + LIBS

    print("Compilation en cours...")
    print(" ".join(cmd))

    try:
        subprocess.check_call(cmd)
        print(f"Compilation réussie ! Exécutable : {output_path}")
    except subprocess.CalledProcessError:
        print("Erreur lors de la compilation.")

if __name__ == "__main__":
    main()
