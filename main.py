import flet as ft
def main(page: ft.Page):
    # Create a Text widget
    text_display = ft.Text(value="Hello, Flet!", size=30)

    # Define the button click function
    def on_button_click(e):
        text_display.value = "Button clicked!"
        page.update()  # Update the page to reflect changes

    # Create a button
    button = ft.ElevatedButton("Click me", on_click=on_button_click)

    # Add widgets to the page
    page.add(text_display, button)


# Run the application
ft.app(target=main)
