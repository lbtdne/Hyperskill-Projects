machine_steps = ["Starting to make a coffee",
                 "Grinding coffee beans",
                 "Boiling water",
                 "Mixing boiled water with crushed coffee beans",
                 "Pouring coffee into the cup",
                 "Pouring some milk into the cup",
                 "Coffee is ready!"]
recipes_ = [[250, 0, 16, 1, -4], [350, 75, 20, 1, -7], [200, 100, 12, 1, -6]]
active_recipe = [0, 0, 0, 0, 0]
machine_levels = [400, 540, 120, 9, 550]
trig_end = False


def request_action():
    global trig_end
    print("Write action (buy, fill, take, remaining, exit):")
    action_ = str(input())
    if action_ == "buy":
        recipe_selector()
        make_coffee()
    elif action_ == "fill":
        fill_machine()
    elif action_ == "take":
        take_money()
    elif action_ == "remaining":
        print_levels()
    elif action_ == "exit":
        trig_end = True


def print_levels():
    global machine_levels
    print("The coffee machine has:")
    print(str(machine_levels[0])
          + " of water")
    print(str(machine_levels[1])
          + " of milk")
    print(str(machine_levels[2])
          + " of coffee beans")
    print(str(machine_levels[3])
          + " of disposable cups")
    print(str(machine_levels[4])
          + " of money")


def fill_machine():
    global machine_levels
    message_ = ["Write how many ml of water do you want to add:",
                "Write how many ml of milk do you want to add:",
                "Write how many grams of coffee beans do you want to add",
                "Write how many disposable cups of coffee do you want to add"]
    for i in range(len(message_)):
        print(message_[i])
        machine_levels[i] = machine_levels[i] + int(input())


def how_many_cups():
    global machine_levels
    global active_recipe
    cups_ = []
    parts_ = ["water", "milk", "coffee beans", "cups"]
    for i in range(len(active_recipe)):
        if active_recipe[i] > 0:
            cups_.append(float(machine_levels[i] / active_recipe[i]))
        else:
            cups_.append(float(1))
    if min(cups_) < 1:
        return parts_[cups_.index(min(cups_))]
    else:
        return "True"


def recipe_selector():
    global recipes_
    global active_recipe
    print("What do you want to buy?\n"
          "1 - espresso\n"
          "2 - latte\n"
          "3 - cappuccino:")
    chosen_ = input()
    if chosen_ == "back":
        request_action()
    else:
        active_recipe = recipes_[int(chosen_) - 1]


def make_coffee():
    global active_recipe
    global machine_levels
    if how_many_cups() == "True":
        print("I have enough resources, making you a coffee!")
        machine_levels = [machine_levels[i] - active_recipe[i] for i in range(len(machine_levels))]
    else:
        print("Sorry, not enough "
              + str(how_many_cups())
              + "!")


def take_money():
    global machine_levels
    print("I gave you $"
          + str(machine_levels[4]))
    machine_levels[4] = 0


while not trig_end:
    request_action()
else:
    exit()