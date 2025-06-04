import subprocess
import sys

def start_lab():
    subprocess.run(["docker-compose", "up", "-d"])

def stop_lab():
    subprocess.run(["docker-compose", "down"])

def reset_lab():
    stop_lab()
    start_lab()

def main():
    if len(sys.argv) < 2:
        print("Usage: python manager.py [start|stop|reset]")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "start":
        start_lab()
    elif cmd == "stop":
        stop_lab()
    elif cmd == "reset":
        reset_lab()
    else:
        print("Unknown command:", cmd)

if __name__ == "__main__":
    main()
