from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


# Function to create the database table if it doesn't exist
def createTable():
    conn = sqlite3.connect('percentile_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS percentiles (
                name TEXT,
                id TEXT PRIMARY KEY,
                rank INTEGER,
                total_participants INTEGER,
                percentage REAL
                )''')
    conn.commit()
    conn.close()


# Function to calculate the percentile and insert data
def insertData():
    try:
        students = int(total_participantField.get())
        rank = int(rankField.get())
        result = round((students - rank) / students * 100, 3)
        messagebox.showinfo("Percentile Result", f"The percentile is: {result}%")

        # Save data to SQLite database
        conn = sqlite3.connect('percentile_data.db')
        c = conn.cursor()

        # Check if the ID already exists
        c.execute("SELECT * FROM percentiles WHERE id=?", (idField.get(),))
        existing_entry = c.fetchone()
        if existing_entry:
            messagebox.showerror("Error", "ID already exists. Please enter a unique ID.")
        else:
            c.execute("INSERT INTO percentiles (name, id, rank, total_participants, percentage) VALUES (?, ?, ?, ?, ?)",
                      (nameField.get(), idField.get(), rank, students, result))
            conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully.")

        conn.close()
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")


# Function for clearing the contents of all text entry boxes
def Clear():
    nameField.delete(0, END)
    idField.delete(0, END)
    rankField.delete(0, END)
    total_participantField.delete(0, END)


# Function to retrieve data from the database
def showData():
    conn = sqlite3.connect('percentile_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM percentiles")
    rows = c.fetchall()
    conn.close()

    # Display data in a pop-up messagebox
    if rows:
        data_str = "\n".join(
            [f"Name: {row[0]}, ID: {row[1]}, Rank: {row[2]}, Total Participants: {row[3]}, Percentage: {row[4]}%" for row in rows])
        messagebox.showinfo("Data", data_str)
    else:
        messagebox.showinfo("Data", "No data available.")


# Function to delete a specific entry from the database by ID
def deleteData():
    id_to_delete = idField.get()
    conn = sqlite3.connect('percentile_data.db')
    c = conn.cursor()
    c.execute("DELETE FROM percentiles WHERE id=?", (id_to_delete,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Data Deleted", f"Data with ID {id_to_delete} has been deleted successfully.")


# Function to update an entry in the database by ID
def updateData():
    try:
        id_to_update = idField.get()
        students = int(total_participantField.get())
        rank = int(rankField.get())
        result = round((students - rank) / students * 100, 3)

        conn = sqlite3.connect('percentile_data.db')
        c = conn.cursor()
        c.execute("UPDATE percentiles SET name=?, rank=?, total_participants=?, percentage=? WHERE id=?",
                  (nameField.get(), rank, students, result, id_to_update))
        conn.commit()
        conn.close()
        messagebox.showinfo("Data Updated", f"Data with ID {id_to_update} has been updated successfully.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")


# Driver Code
if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Create the database table
    createTable()

    # Load the image using PIL
    try:
        pil_image = Image.open("education.jpg")
    except FileNotFoundError:
        messagebox.showerror("Error",
                             "Image file not found. Please make sure 'education.jpg' is in the same directory as this script.")
        gui.destroy()
        exit()

    background_image = ImageTk.PhotoImage(pil_image)

    # Create a Canvas widget
    canvas = Canvas(gui, width=background_image.width(), height=background_image.height())
    canvas.pack(fill="both", expand=True)

    # Display the image on the canvas
    canvas.create_image(0, 0, image=background_image, anchor="nw")

    # Set the name of tkinter GUI window
    gui.title("Rank Based- Percentile Calculator")

    # Set the configuration of GUI window
    gui.geometry(f"{background_image.width()}x{background_image.height()}")

    # Define widget widths for alignment
    entry_width = 200
    label_width = 150
    button_width = 150
    vertical_spacing = 50
    button_spacing = 20

    # Define starting x and y positions
    start_x = 50
    start_y = 50

    # Create the widgets
    name = Label(gui, text="Name", bg="white")
    nameField = Entry(gui)
    id_label = Label(gui, text="ID", bg="white")
    idField = Entry(gui)
    rank = Label(gui, text="Rank", bg="white")
    rankField = Entry(gui)
    total_participant = Label(gui, text="Total Participants", bg="white")
    total_participantField = Entry(gui)
    insert_btn = Button(gui, text="Save Data", fg="black", bg="white", command=insertData)
    clear = Button(gui, text="Clear", fg="Black", bg="white", command=Clear)
    show_data_btn = Button(gui, text="Show Data", fg="Black", bg="white", command=showData)
    delete_data_btn = Button(gui, text="Delete Data", fg="Black", bg="white", command=deleteData)
    update_data_btn = Button(gui, text="Update Data", fg="Black", bg="white", command=updateData)

    # Place the buttons on the canvas at the top
    button_start_x = 50
    button_start_y = 10
    button_vertical_spacing = 40

    canvas.create_window(button_start_x, button_start_y, window=insert_btn, width=button_width, anchor="nw")
    canvas.create_window(button_start_x + button_width + button_spacing, button_start_y, window=show_data_btn, width=button_width, anchor="nw")
    canvas.create_window(button_start_x + 2 * (button_width + button_spacing), button_start_y, window=delete_data_btn, width=button_width, anchor="nw")
    canvas.create_window(button_start_x + 3 * (button_width + button_spacing), button_start_y, window=update_data_btn, width=button_width, anchor="nw")

    # Adjust starting positions for the entry fields and labels
    start_y = button_start_y + button_vertical_spacing + vertical_spacing
    # Place the widgets on the canvas, line by line
    current_y = start_y
    canvas.create_window(start_x, current_y, window=name, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=nameField, width=entry_width, anchor="nw")

    current_y += vertical_spacing
    canvas.create_window(start_x, current_y, window=id_label, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=idField, width=entry_width, anchor="nw")

    current_y += vertical_spacing
    canvas.create_window(start_x, current_y, window=rank, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=rankField, width=entry_width, anchor="nw")

    current_y += vertical_spacing
    canvas.create_window(start_x, current_y, window=total_participant, anchor="nw")
    canvas.create_window(start_x + label_width, current_y, window=total_participantField, width=entry_width, anchor="nw")

    current_y += vertical_spacing
    canvas.create_window(start_x, current_y, window=clear, width=button_width, anchor="nw")

    # Prevent image garbage collection
    gui.background_image = background_image

    # Start the GUI
    gui.mainloop()
