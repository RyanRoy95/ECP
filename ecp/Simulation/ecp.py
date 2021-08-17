
from cc3d import CompuCellSetup
        

from ecpSteppables import ecpSteppable

CompuCellSetup.register_steppable(steppable=ecpSteppable(frequency=1))


CompuCellSetup.run()
