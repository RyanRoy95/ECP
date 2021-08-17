
from cc3d.core.PySteppables import *

class ecpSteppable(SteppableBasePy):

    def __init__(self,frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        any code in the start function runs before MCS=0
        """
        
        
        
        for i in range(19,79):
            x = i
            y = 19
            size = 2
            cell = self.new_cell(self.APICAL)
            # size of cell will be SIZExSIZEx1
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
            
            b = 79
            cell = self.new_cell(self.BASAL)
            self.cell_field[x:x + size - 1, b:b + size - 1, 0] = cell
            
            
        for i in range(19,79):
            y = i
            x = 19
            size = 2
            cell = self.new_cell(self.TESTUBE)
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
            x = 78
            cell = self.new_cell(self.TESTUBE)
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
            
        for i in range(1,99):
            x = i
            y = 1
            cell = self.new_cell(self.TESTUBE)
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
            
            x = 1
            y = i
            cell = self.new_cell(self.TESTUBE)
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
            
            x = i
            y = 98
            cell = self.new_cell(self.TESTUBE)
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
            
            x = 98
            y = i
            cell = self.new_cell(self.TESTUBE)
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
            

            
            
            
            
            
            
         
                
               
                
               
            

            
            
            
        
            
        

    def step(self,mcs):
        """
        type here the code that will run every frequency MCS
        :param mcs: current Monte Carlo step
        """

        for cell in self.cell_list:

            print("cell.id=",cell.id)

    def finish(self):
        """
        Finish Function is called after the last MCS
        """

    def on_stop(self):
        # this gets called each time user stops simulation
        return


        