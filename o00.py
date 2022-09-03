class Tiger:
    def run_n_growl(self):
        self.run(distance=50)
        self.growl()

    def run(self, distance):
        print(f'tiger is running {distance}m')

    def growl(self):
        print('tiger is growling: rrrr')

if __name__ == '__main__':
    # print(type(Tiger))
    # print(Tiger.__class__)
    tiger1 = Tiger()
    # print(tiger1)
    # print(type(tiger1))
    # print(tiger1.__class__.__name__ == 'Tiger')
    # print(isinstance(tiger1, Tiger))
    # Tiger.run(self=tiger1)
    # tiger1.run(distance=100)
    # tiger1.growl()
    tiger2 = Tiger()
    # tiger2.growl()
    tiger2.run_n_growl()