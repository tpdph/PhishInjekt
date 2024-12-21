import tkinter as tk
from tkinter import ttk
from explorer import setup_explorer_gui
from injektor import setup_injektor_gui
from phisher import setup_phisher_gui, app
from brutus.brutus import setup_brutus_gui
import threading
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='phishinjekt.log'
)
logger = logging.getLogger(__name__)

class PhishInjektApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PhishInjekt")
        self.setup_gui()

    def setup_gui(self):
        try:
            notebook = ttk.Notebook(self.root)
            notebook.pack(pady=10, padx=10, expand=True, fill='both')

            # Create tabs
            tabs = {
                'Explorer': setup_explorer_gui,
                'Injektor': setup_injektor_gui,
                'Phisher': setup_phisher_gui,
                'Brutus': setup_brutus_gui
            }

            for name, setup_func in tabs.items():
                tab = ttk.Frame(notebook)
                notebook.add(tab, text=name)
                setup_func(tab)

        except Exception as e:
            logger.error(f"Error setting up GUI: {e}")
            raise

    def run(self):
        try:
            threading.Thread(target=app.run, kwargs={'debug': False, 'host': '0.0.0.0'}, daemon=True).start()
            self.root.mainloop()
        except Exception as e:
            logger.error(f"Error running application: {e}")
            raise

def main():
    try:
        phish_app = PhishInjektApp()
        phish_app.run()
    except Exception as e:
        logger.critical(f"Critical error in main: {e}")
        raise

if __name__ == "__main__":
    main()
