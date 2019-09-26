class Renderer:
    """ a renderer class """
    minecraft: mc.Minecraft = None
    session: Session = None
    prev_session: Session = None

    def __init__(self, _mc: mc.Minecraft, sc: Session) -> None:
        self.minecraft = _mc
        self.session = sc

    def render(self):
    """ Render Session to Minecraft world. """
    pass
