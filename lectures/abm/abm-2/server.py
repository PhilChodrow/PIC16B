"""
A definition of the server used to visualize a simple Schelling model. 
Run by navigating to the directory containing this file and run 
>>> conda activate PIC16B
>>> mesa runserver
in the command line. For this to work, it is also necessary to install
mesa to the PIC16B conda environment: 
>>> conda activate PIC16B
>>> conda install -c conda-forge mesa
"""

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter

from model import SchellingModel

# a simple string display element
class MoveElement(TextElement):
    """
    Display a text count of how many happy agents there are.
    """

    def __init__(self):
        pass

    def render(self, model):
        return f"Agents moving: {model.moved}."

move_element = MoveElement()

# main display element: a grid showing the model state
# the portrayal is a set of aesthetic parameters
# applied to each agent in the model
def schelling_draw(agent):
    """
    Portrayal Method for canvas
    """
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0, "stroke_color" : "#4a4a4a"}

    if agent.type == "Orange":
        portrayal["Color"] = ["#ff962e", "#ff962e"]
    else:
        portrayal["Color"] = ["#2ee0ff", "#2ee0ff"]
    return portrayal

# 20x20 grid of 400x400 pixels, with agents rendered
# using the above function
canvas_element = CanvasGrid(schelling_draw, 20, 20, 400, 400)

# a simple timeseries visualization
move_chart = ChartModule([{"Label": "num_moved", "Color": "Black"}])


# parameters passed to the model
# passing parameter "values" equal to UserSettableParameters creates
# pleasant sliders
model_params = {
    "height": 20,
    "width": 20,
    "density": UserSettableParameter("slider", "Agent density", 0.8, 0.1, 1.0, 0.1),
    "homophily": UserSettableParameter("slider", "homophily", 0.5, 0.0, 1.0, .02),
}

# serve the different model elements
server = ModularServer(
    SchellingModel,                             # model used
    [move_element, canvas_element,  move_chart], # elements rendered
    "Schelling Model Visualization",            # name
    model_params                                # parameters of model
)