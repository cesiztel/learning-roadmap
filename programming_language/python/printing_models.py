def print_models(unprinted_designs):
    """
    Simulates printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    completed_models = []
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    
    return completed_models

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

# Copying the array to keep the pure the function
completed_models = print_models(unprinted_designs[:]) 
show_completed_models(completed_models)