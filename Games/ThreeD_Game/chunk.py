class ChunkManager:
    def __init__(self):
        self.chunk_size = 5
        self.tile_size = 1
        self.render_distance = 0
        self.loaded_chunks = {}

    def generate_chunk(self , chunk_x , chunk_z):
        if (chunk_x , chunk_z) in self.loaded_chunks:
            return
        tiles = []

        for x in range(self.chunk_size):
            for z in range(self.chunk_size):
                offset = self.chunk_size//2
                world_x = (chunk_x * self.chunk_size + x) - offset
                world_z = (chunk_z * self.chunk_size + z) - offset
                tiles.append((world_x , world_z))
        self.loaded_chunks[(chunk_x , chunk_z)] = tiles

    def update_chunks(self , player_chunk_x , player_chunk_z , direction = None):
        needed_chunks = set()
        for dx in range(-self.render_distance , self.render_distance+1):
            for dz in range(-self.render_distance , self.render_distance+1):
                chunk_x = player_chunk_x + dx
                chunk_z = player_chunk_z + dz
                needed_chunks.add((chunk_x , chunk_z))

                if (chunk_x , chunk_z) not in self.loaded_chunks:
                    self.generate_chunk(chunk_x , chunk_z)

        for chunk in list(self.loaded_chunks.keys()):
            if chunk not in needed_chunks:
                self.loaded_chunks.pop(chunk , None)
