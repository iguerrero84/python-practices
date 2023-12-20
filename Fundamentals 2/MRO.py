class Top:
    def m_top(self):
        print("superior")


class Middle(Top):
    def m_middle(self):
        print("medio")


class Bottom(Top, Middle):
    def m_bottom(self):
        print("abajo")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
