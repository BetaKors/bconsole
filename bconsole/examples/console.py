from bconsole import Console, Foreground, Modifier

console = Console()

console.print("Hello World!", Foreground.WHITE + Modifier.BOLD)
console.print(
    "You can make completely custom colors too!",
    Foreground.make_rgb(255, 128, 30),  # not supported in all terminals
)
name = console.input("What is your name?")

console.print(f"Hello, {name}!", Foreground.make(31))  # same as Foreground.RED

console.space()

print(console.options("Do you like the color red?"))

if console.options("Do you like the color red?") == "Yes":  # defaults to Yes/No
    console.print("Me too!")
else:
    console.print("Well, I do!")

if (
    console.options(
        "Which animal do you prefer, cats or dogs?", options=["cats", "dogs"]
    )
    == "cats"
):
    console.print("Meow!")
else:
    console.print("Woof!")

for i in range(3):
    console.print(f"This is line number {i + 1}.")

console.erase_lines(2)

console.arrow("I just did something important!")

console.error("Something went wrong!", hint="Maybe you should try again?")
console.panic("Something went really wrong!", code=-1)
console.print("This will not be printed.")
