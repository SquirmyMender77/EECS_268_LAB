class Pokemon:
    def __init__(self, cur_a_name, cur_poke_id, cur_j_name):
        self.a_name = cur_a_name
        self._id = cur_poke_id
        self.j_name = cur_j_name

    def __lt__(self, other):
        if isinstance(other, Pokemon):
            return self._id < other._id

        if isinstance(other, int):
            return self._id < other

        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Pokemon):
            return self._id > other._id

        if isinstance(other, int):
            return self._id > other

        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Pokemon):
            return self._id == other._id

        if isinstance(other, int):
            return self._id == other

        return NotImplemented

    def __str__(self):
        return(f"{self.a_name},{self._id},{self.j_name}")
