import qrcode
from typing import Optional

DEFAULT_FILL = "black"
DEFAULT_BACK = "white"

ALLOWED_COLORS = [
    "black", "white", "gray", "red", "green", "blue", "yellow",
    "orange", "purple", "pink", "brown", "cyan", "magenta",
    "lime", "navy", "gold", "silver"
]

MENU = (
    "Wpisz:\n"
    "  start     — utwórz kod QR z domyślnymi kolorami\n"
    "  settings  — wybierz kolory i utwórz kod QR\n"
    "  exit      — zakończ program\n"
)

def make_qr_image(
    data: str,
    fill_color: str = DEFAULT_FILL,
    back_color: str = DEFAULT_BACK,
    box_size: int = 10,
    border: int = 4,
):

    qr = qrcode.QRCode(
        version=5,
        box_size=box_size,
        border=border,

    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    return img

def prompt_text(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Pole nie może być puste. Spróbuj ponownie.")

def prompt_color(prompt: str) -> str:
    print(f"Przykładowe kolory: {ALLOWED_COLORS}")
    while True:
        c = input(prompt).strip().lower()
        if c in ALLOWED_COLORS:
            return c
        print("Nieznany kolor. Wybierz z listy powyżej.")

def handle_start_flow():
    text = prompt_text("Podaj treść/link do umieszczenia w kodzie QR: ")
    img = make_qr_image(text, DEFAULT_FILL, DEFAULT_BACK, version=5)
    img.show()
    print("✅ Wygenerowano kod QR (domyślne kolory).")

def handle_settings_flow():
    print("Ustawienia kolorów kodu QR")
    text = prompt_text("Podaj treść/link do umieszczenia w kodzie QR: ")
    fill = prompt_color("Kolor wypełnienia: ")
    back = prompt_color("Kolor tła: ")
    img = make_qr_image(text, fill, back, version=5)
    img.show()
    print(f"✅ Wygenerowano kod QR (wypełnienie: {fill}, tło: {back}).")

def main():
    print("QR Code Generator")
    print("=" * 50)

    while True:
        print(MENU)
        cmd = input("> ").strip().lower()

        if cmd == "exit":
            print("Koniec programu.")
            break
        elif cmd == "start":
            handle_start_flow()
        elif cmd == "settings":
            handle_settings_flow()
        else:
            print("Nie rozpoznano komendy. Spróbuj: start / settings / exit")
            continue

        again = input("Wprowadź 'y' aby wrócić do menu, 'q' aby zakończyć: ").strip().lower()
        if again != "y":
            print("Koniec programu.")
            break

if __name__ == "__main__":
    main()
