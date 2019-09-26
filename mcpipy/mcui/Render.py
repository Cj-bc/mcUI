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


def diff(prev: Sesssion, new: Session) -> Tuple[Pane, Pane]:
    """Pick up changed panes and return them as one list
    """
    added: List[Pane]   = filter(lambda p: not p in prev.panes, new.panes)
    rmv_tmp: List[Pane] = filter(lambda p: not p in new.panes, prev.panes)
    removed: List[Pane] = map(lambda p: map(lambda e: e.setNoBlock(), p.entries)
                 , rmv_tmp)
    return (added, removed)

