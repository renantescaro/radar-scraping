import time
import subprocess
import sys


def main():
    while True:
        print("--- Iniciando Coleta ---")
        try:
            subprocess.run([sys.executable, "run.py"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar run.py: {e}")

        # 30 min 1800
        # 10 min 600
        time.sleep(600)


if __name__ == "__main__":
    main()
