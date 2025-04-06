from enum import Enum
from pydantic import BaseModel

###########################################
### ------- Enums for Selections ------ ###
###########################################

class NodeIdentifier(str, Enum):
    # index of the Node in the list of all nodes of one Namespace
    list_index = "index"
    # unique and distinct name of a parameter
    metric_name = "metric"
    # common name that is used in daily business
    trivial_name = "trivial"
    # unique and distinct identifier in the context of data source
    node_id = "node-id"


###########################################
### ------ Defining Request Bodys ----- ###
###########################################

class Connection(BaseModel):
    # host adress to a server 
    host: str
    # port to use with the host
    port: int

class DataNode(BaseModel):
    # name of the data service
    name: str 
    # organisation which owns the service
    organisation: str 
    # connection information of the service
    connection: Connection

class DataSourceSecurity(BaseModel):
    # policy of an opcua connection
    policy: str
    # mode of an opcua connection
    mode: str

class DataSourceConnection(Connection):
    # adding security attribute to Connection
    security: DataSourceSecurity

class DataSource(DataNode):
    # connection information for a data source
    connection: DataSourceConnection
    # rate in which new data is requested
    reading_rate: float

class DataSinkConnection(Connection):
    # time a connection is to be held alive
    keepalive: int 

class DataSink(DataNode):
    # connection to a data sink
    connection: DataSinkConnection

class DeleteNodeRequest(BaseModel):
    # attribute by which the node should be removed
    delete_by: NodeIdentifier
    # Value that the attribute of the node to be deleted should assume
    identifier: str | int

class WriteNodeRequest(BaseModel):
    # unique and distinct name of a parameter
    metric_name: str
    # common name that is used in daily business
    trivial_name: str
    # unit in which measurement is taken in 
    unit: str
    # unique and distinct identifier in the context of data source
    node_id: str