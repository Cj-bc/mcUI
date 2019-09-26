from mcUI.entry import Pane, Session
from copy import deepcopy

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
        plus, minus = diff(self.prev_session, self.session)
        schemas = schema

        for p in plus + minus:
            for entry, pos in zip(p.entries,
                                  calc_entries_coordinate(p, padding, line_vec, MAX_OBJECT_PER_LINE)):
                entry.sevePos(pos)

        map(lambda p: map(_writeEntry, p.entries), plus)
        map(lambda p: map(_removeEntry, p.entries), minus)
        self.prev_session = deepcopy(self.session)

    @staticmethod
    def _writeEntry(e: Entry) -> None:
        mc.setBlock(entry.pos.x, entry.pos.y, entry.pos.z, schemas[e.filetype])
        ent_id = mc.spawnEntity(entity.ARMORSTAND, e.pos,
                                '{CustomName: ' + e.filename + \
                                ', CustomNameVisible: true, NoGravity: true, Invisible: true}')
        e.saveNameEntityId(ent_id)

    @staticmethod
    def _removeEntry(e: Entry) -> None:
        mc.setBlock(e.pos.x, e.pos.y, e.pos.z, block.AIR)
        mc.removEntity(e.nameEntityId)


def diff(prev: Sesssion, new: Session) -> Tuple[Pane, Pane]:
    """Pick up changed panes and return them as one list
    """
    added: List[Pane]   = filter(lambda p: not p in prev.panes, new.panes)
    rmv_tmp: List[Pane] = filter(lambda p: not p in new.panes, prev.panes)
    removed: List[Pane] = map(lambda p: map(lambda e: e.setNoBlock(), p.entries)
                 , rmv_tmp)
    return (added, removed)

