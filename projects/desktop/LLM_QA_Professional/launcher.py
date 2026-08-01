from app.bootstrap import bootstrap

def launch():
    state = bootstrap()
    print("System Ready:", state)

if __name__ == "__main__":
    launch()