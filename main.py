import random


class Blob:
    def __init__(self, birth, death, replication, mutation):
        self.birth = birth
        self.death = death
        self.replication = replication
        self.mutation = mutation

    def get_birth(self):
        return self.birth

    def get_death(self):
        return self.death

    def get_replication(self):
        return self.replication

    def get_mutation(self):
        return self.mutation


def simulation(times):
    blue_blob_population = 0
    green_blob_population = 0
    while times > 0:
        death_test = green_blob_population
        while death_test > 0:
            death = random.randrange(1, 101)
            if death <= green_blob.get_death():
                green_blob_population -= 1
            death_test -= 1
        replication_test = green_blob_population

        while replication_test > 0:
            replication = random.randrange(1, 101)
            if replication <= green_blob.get_replication():
                mutation = random.randrange(1, 101)
                if mutation <= green_blob.get_mutation():
                    blue_blob_population += 1
                else:
                    green_blob_population += 1
            replication_test -= 1
        death_test = blue_blob_population

        while death_test > 0:
            death = random.randrange(1, 101)
            if death <= blue_blob.get_death():
                blue_blob_population -= 1
            death_test -= 1
        replication_test = blue_blob_population

        while replication_test > 0:
            replication = random.randrange(1, 101)
            if replication <= blue_blob.get_replication():
                mutation = random.randrange(1, 101)
                if mutation <= blue_blob.get_mutation():
                    green_blob_population += 1
                else:
                    blue_blob_population += 1
            replication_test -= 1
        spawn = random.randrange(1, 101)
        if spawn <= blue_blob.get_birth():
            blue_blob_population += 1
        print(f"Green population: {green_blob_population}")
        print(f"Blue population: {blue_blob_population}")
        print("")
        times -= 1


blue_blob = Blob(100, 10, 5, 10)
green_blob = Blob(0, 20, 10, 0)

simulation(2000)
