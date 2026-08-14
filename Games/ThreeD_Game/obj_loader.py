class OBJLoader:
    def __init__(self):
        self.vertices = []
        self.texture_vertices = []
        self.normals = []
        self.faces = []
        self.material = None
        self.groups = {}
        self.current_group = "default"

    def load(self , filename):
        try:
            with open(filename , "r") as file:
                lines = file.readlines()
            print("File loaded successfully ")
            print("Total Lines :" , len(lines))
            for line in lines:
                line = line.strip()
                if line.startswith("g "):
                    self.current_group = line.split()[1]
                    if self.current_group not in self.groups:
                        self.groups[self.current_group] = {
                            "faces" :  [],
                            "vertices" : set()
                        }
                        continue
                line = line.strip()
                if line.startswith("v "):
                    values = line.split()
                    if len(values) >= 4:
                        x = float(values[1])
                        y = float(values[2])
                        z = float(values[3])

                        self.vertices.append((x,y,z))
                elif line.startswith("f "):
                    values = line.split()[1:]
                    face = []
                    for value in values:
                        vertex_index = int(value.split("/")[0]) - 1
                        face.append(vertex_index)
                        self.groups[self.current_group]["vertices"].add(vertex_index)
                        self.faces.append(face)
                        self.groups[self.current_group]["faces"].append(face)
            self.calculate_pivot()
        except Exception as e:
            print(e)

    def calculate_pivot(self):
        self.pivots = {}
        for group_name  , group_data in self.groups.items():
            xs = []
            ys = []
            zs = []
            for index in group_data["vertices"]:
                vx  , vy , vz = self.vertices[index]

                xs.append(vx)
                ys.append(vy)
                zs.append(vz)

            if len(xs) == 0:
                continue
            pivot_x = (min(xs) + max(xs)) / 2
            pivot_y = max(ys)
            pivot_z = (min(zs) + max(zs))

            self.pivots[group_name] = (
                pivot_x , pivot_y , pivot_z
            )