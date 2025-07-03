# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)]
# From type library 'RpcSinumerik.ocx'
# On Wed Jul 31 12:26:36 2024
'RPC SINUMERIK.OCX 1.00 RPC SINUMERIK control'
makepy_version = '0.5.01'
python_version = 0x30b06f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{03B415E0-4F2E-11D3-9DC3-00A0249B4877}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IMachine(DispatchBaseClass):
	'IMachine Interface'
	CLSID = IID('{EDF199C0-4F2E-11D3-9DC3-00A0249B4877}')
	coclass_clsid = IID('{EDF199C1-4F2E-11D3-9DC3-00A0249B4877}')

	def C_DELETE_M(self, OrderNum=defaultNamedNotOptArg, SFkt=defaultNamedNotOptArg, Name1=defaultNamedNotOptArg, Name2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), ((3, 1), (3, 1), (16392, 1), (16392, 1)),OrderNum
			, SFkt, Name1, Name2)

	def C_MODE_M(self, OrderNum=defaultNamedNotOptArg, Mode=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(21, LCID, 1, (3, 0), ((3, 1), (3, 1)),OrderNum
			, Mode)

	def C_ORDER_M(self, OrderNum=defaultNamedNotOptArg, SFkt=defaultNamedNotOptArg, Name1=defaultNamedNotOptArg, Name2=defaultNamedNotOptArg
			, Name3=defaultNamedNotOptArg, Name4=defaultNamedNotOptArg, Parameter1=defaultNamedNotOptArg, Parameter2=defaultNamedNotOptArg, Parameter3=defaultNamedNotOptArg
			, Parameter4=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(25, LCID, 1, (3, 0), ((3, 1), (3, 1), (16392, 1), (16392, 1), (16392, 1), (16392, 1), (3, 1), (3, 1), (3, 1), (3, 1)),OrderNum
			, SFkt, Name1, Name2, Name3, Name4
			, Parameter1, Parameter2, Parameter3, Parameter4)

	def C_SYNCH_M(self, OrderNum=defaultNamedNotOptArg, SynchFlag=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(22, LCID, 1, (3, 0), ((3, 1), (3, 1)),OrderNum
			, SynchFlag)

	def C_TPORDER_M(self, OrderNum=defaultNamedNotOptArg, SDockPos=defaultNamedNotOptArg, DDockPos=defaultNamedNotOptArg, WPC=defaultNamedNotOptArg
			, WPCTyp=defaultNamedNotOptArg, BufferFlag=defaultNamedNotOptArg, Priority=defaultNamedNotOptArg, ChainNum=defaultNamedNotOptArg, Vehicle=defaultNamedNotOptArg
			, ResInt1=defaultNamedNotOptArg, ResInt2=defaultNamedNotOptArg, ResByte=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(23, LCID, 1, (3, 0), ((3, 1), (3, 1), (3, 1), (16392, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (16392, 1)),OrderNum
			, SDockPos, DDockPos, WPC, WPCTyp, BufferFlag
			, Priority, ChainNum, Vehicle, ResInt1, ResInt2
			, ResByte)

	def R_DATA_M(self, OrderNum=defaultNamedNotOptArg, SFkt=defaultNamedNotOptArg, Name1=defaultNamedNotOptArg, Name2=defaultNamedNotOptArg
			, Date=defaultNamedNotOptArg, LastFile=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(17, LCID, 1, (3, 0), ((3, 1), (3, 1), (16392, 1), (16392, 1), (3, 1), (3, 1)),OrderNum
			, SFkt, Name1, Name2, Date, LastFile
			)

	def R_DDEDATA_M(self, OrderNum=defaultNamedNotOptArg, Application=defaultNamedNotOptArg, Topic=defaultNamedNotOptArg, Item=defaultNamedNotOptArg
			, Data=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((3, 1), (16392, 1), (16392, 1), (16392, 1), (16392, 1)),OrderNum
			, Application, Topic, Item, Data)

	def R_MESSAGE_M(self, OrderNum=defaultNamedNotOptArg, Message=defaultNamedNotOptArg, ResInt1=defaultNamedNotOptArg, ResInt2=defaultNamedNotOptArg
			, ResByte=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((3, 1), (16392, 1), (3, 1), (3, 1), (16392, 1)),OrderNum
			, Message, ResInt1, ResInt2, ResByte)

	def R_NC4WPC_M(self, OrderNum=defaultNamedNotOptArg, WPC=defaultNamedNotOptArg, NCProg=defaultNamedNotOptArg, DateVal=defaultNamedNotOptArg
			, NCPLength=defaultNamedNotOptArg, ClampCubeSide=defaultNamedNotOptArg, TpFlag=defaultNamedNotOptArg, NCExtern=defaultNamedNotOptArg, ResInt1=defaultNamedNotOptArg
			, ResInt2=defaultNamedNotOptArg, ResByte=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(14, LCID, 1, (3, 0), ((3, 1), (16392, 1), (16392, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (16392, 1)),OrderNum
			, WPC, NCProg, DateVal, NCPLength, ClampCubeSide
			, TpFlag, NCExtern, ResInt1, ResInt2, ResByte
			)

	def R_REPORT_M(self, OrderNum=defaultNamedNotOptArg, Typ=defaultNamedNotOptArg, Number=defaultNamedNotOptArg, ResInt1=defaultNamedNotOptArg
			, ResInt2=defaultNamedNotOptArg, ResByte=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(15, LCID, 1, (3, 0), ((3, 1), (3, 1), (3, 1), (3, 1), (3, 1), (16392, 1)),OrderNum
			, Typ, Number, ResInt1, ResInt2, ResByte
			)

	def R_VAR_M(self, OrderNum=defaultNamedNotOptArg, VarMode=defaultNamedNotOptArg, VarSet=defaultNamedNotOptArg, VarDescr=defaultNamedNotOptArg
			, VarData=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(18, LCID, 1, (3, 0), ((3, 1), (3, 1), (16392, 1), (16392, 1), (16392, 1)),OrderNum
			, VarMode, VarSet, VarDescr, VarData)

	def Shutdown_M(self):
		return self._oleobj_.InvokeTypes(24, LCID, 1, (24, 0), (),)

	def T_DATA_M(self, OrderNum=defaultNamedNotOptArg, SFkt=defaultNamedNotOptArg, Name1=defaultNamedNotOptArg, Name2=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((3, 1), (3, 1), (16392, 1), (16392, 1)),OrderNum
			, SFkt, Name1, Name2)

	def T_MACHINE_M(self, OrderNum=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(10, LCID, 1, (3, 0), ((3, 1),),OrderNum
			)

	def T_REPORT_M(self, OrderNum=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(26, LCID, 1, (3, 0), ((3, 1),),OrderNum
			)

	def T_TPS_M(self, OrderNum=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(11, LCID, 1, (3, 0), ((3, 1),),OrderNum
			)

	def T_VAR_M(self, OrderNum=defaultNamedNotOptArg, VarMode=defaultNamedNotOptArg, VarSet=defaultNamedNotOptArg, VarDescr=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((3, 1), (3, 1), (16392, 1), (16392, 1)),OrderNum
			, VarMode, VarSet, VarDescr)

	_prop_map_get_ = {
		"HostEnabled": (7, 2, (11, 0), (), "HostEnabled", None),
		"HostID": (5, 2, (8, 0), (), "HostID", None),
		"HostPort": (6, 2, (3, 0), (), "HostPort", None),
		"MachineID": (1, 2, (8, 0), (), "MachineID", None),
		"MachineIP": (2, 2, (8, 0), (), "MachineIP", None),
		"MachinePort": (3, 2, (3, 0), (), "MachinePort", None),
		"MachineTimeout": (4, 2, (2, 0), (), "MachineTimeout", None),
	}
	_prop_map_put_ = {
		"HostEnabled": ((7, LCID, 4, 0),()),
		"HostID": ((5, LCID, 4, 0),()),
		"HostPort": ((6, LCID, 4, 0),()),
		"MachineID": ((1, LCID, 4, 0),()),
		"MachineIP": ((2, LCID, 4, 0),()),
		"MachinePort": ((3, LCID, 4, 0),()),
		"MachineTimeout": ((4, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _IMachineEvents:
	'_IMachineEvents Interface'
	CLSID = CLSID_Sink = IID('{EDF199C2-4F2E-11D3-9DC3-00A0249B4877}')
	coclass_clsid = IID('{EDF199C1-4F2E-11D3-9DC3-00A0249B4877}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		       10 : "OnRxMACHINExH",
		       11 : "OnRxTPSxH",
		       12 : "OnRxREPORTxH",
		       13 : "OnRxMESSAGExH",
		       14 : "OnTxDATAxH",
		       15 : "OnRxDATAxH",
		       16 : "OnTxVARxH",
		       17 : "OnRxVARxH",
		       18 : "OnRxDDEDATAxH",
		       19 : "OnShutdownH",
		       20 : "OnRxREPORTxH2",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
	# def OnRxMACHINExH(self, OrderNum=defaultNamedNotOptArg, MachineMode=defaultNamedNotOptArg, MachineStatus=defaultNamedNotOptArg, NCProgramm=defaultNamedNotOptArg
	# 		, ClampCubeSide=defaultNamedNotOptArg, DockPos1=defaultNamedNotOptArg, DockPos2=defaultNamedNotOptArg, DockPos3=defaultNamedNotOptArg, DockPosStatus1=defaultNamedNotOptArg
	# 		, DockPosStatus2=defaultNamedNotOptArg, DockPosStatus3=defaultNamedNotOptArg, WPC1=defaultNamedNotOptArg, WPC2=defaultNamedNotOptArg, WPC3=defaultNamedNotOptArg
	# 		, WPCStatus1=defaultNamedNotOptArg, WPCStatus2=defaultNamedNotOptArg, WPCStatus3=defaultNamedNotOptArg, ResInt1=defaultNamedNotOptArg, ResInt2=defaultNamedNotOptArg
	# 		, ResByte=defaultNamedNotOptArg):
	# 	print("OnRxMACHINExH")
	# def OnRxTPSxH(self, OrderNum=defaultNamedNotOptArg, MachineMode=defaultNamedNotOptArg, MachineStatus=defaultNamedNotOptArg, TpOStatus=defaultNamedNotOptArg
	# 		, DockPos1=defaultNamedNotOptArg, DockPos2=defaultNamedNotOptArg, DockPosStatus1=defaultNamedNotOptArg, DockPosStatus2=defaultNamedNotOptArg, WPC1=defaultNamedNotOptArg
	# 		, WPC2=defaultNamedNotOptArg, ResInt1=defaultNamedNotOptArg, ResInt2=defaultNamedNotOptArg, ResByte=defaultNamedNotOptArg):
	# 	print("OnRxTPSxH")
	# def OnRxREPORTxH(self, OrderNum=defaultNamedNotOptArg, Typ=defaultNamedNotOptArg, Number=defaultNamedNotOptArg, Time=defaultNamedNotOptArg
	# 		, Flag=defaultNamedNotOptArg, ResInt1=defaultNamedNotOptArg, ResInt2=defaultNamedNotOptArg, ResByte=defaultNamedNotOptArg):
	# 	print("OnRxREPORTxH")
	# def OnRxMESSAGExH(self, OrderNum=defaultNamedNotOptArg, Message=defaultNamedNotOptArg, ResInt1=defaultNamedNotOptArg, ResInt2=defaultNamedNotOptArg
	# 		, ResByte=defaultNamedNotOptArg):
	# 	print("OnRxMESSAGExH")
	# def OnTxDATAxH(self, OrderNum=defaultNamedNotOptArg, SFkt=defaultNamedNotOptArg, Name1=defaultNamedNotOptArg, Name2=defaultNamedNotOptArg):
	# 	print("OnTxDATAxH")
	# def OnRxDATAxH(self, OrderNum=defaultNamedNotOptArg, SFkt=defaultNamedNotOptArg, Name1=defaultNamedNotOptArg, Name2=defaultNamedNotOptArg
	# 		, DateVal=defaultNamedNotOptArg, LastFile=defaultNamedNotOptArg):
	# 	print("OnRxDATAxH")
	# def OnTxVARxH(self, OrderNum=defaultNamedNotOptArg, VarMode=defaultNamedNotOptArg, VarSet=defaultNamedNotOptArg, VarDescr=defaultNamedNotOptArg):
	# 	print("OnTxVARxH")
	# def OnRxVARxH(self, OrderNum=defaultNamedNotOptArg, VarMode=defaultNamedNotOptArg, VarSet=defaultNamedNotOptArg, VarDescr=defaultNamedNotOptArg
	# 		, VarData=defaultNamedNotOptArg):
	# 	print("OnRxVARxH")
	# def OnRxDDEDATAxH(self, OrderNum=defaultNamedNotOptArg, Data=defaultNamedNotOptArg):
	# 	print("OnRxDDEDATAxH")
	# def OnShutdownH(self):
	# 	print("OnShutdownH")
	# def OnRxREPORTxH2(self, OrderNum=defaultNamedNotOptArg, Typ=defaultNamedNotOptArg, Number1=defaultNamedNotOptArg, Number2=defaultNamedNotOptArg
	# 		, Number3=defaultNamedNotOptArg, Number4=defaultNamedNotOptArg, Number5=defaultNamedNotOptArg, Number6=defaultNamedNotOptArg, Number7=defaultNamedNotOptArg
	# 		, Number8=defaultNamedNotOptArg, Number9=defaultNamedNotOptArg, Number10=defaultNamedNotOptArg, Time1=defaultNamedNotOptArg, Time2=defaultNamedNotOptArg
	# 		, Time3=defaultNamedNotOptArg, Time4=defaultNamedNotOptArg, Time5=defaultNamedNotOptArg, Time6=defaultNamedNotOptArg, Time7=defaultNamedNotOptArg
	# 		, Time8=defaultNamedNotOptArg, Time9=defaultNamedNotOptArg, Time10=defaultNamedNotOptArg, Flag1=defaultNamedNotOptArg, Flag2=defaultNamedNotOptArg
	# 		, Flag3=defaultNamedNotOptArg, Flag4=defaultNamedNotOptArg, Flag5=defaultNamedNotOptArg, Flag6=defaultNamedNotOptArg, Flag7=defaultNamedNotOptArg
	# 		, Flag8=defaultNamedNotOptArg, Flag9=defaultNamedNotOptArg, Flag10=defaultNamedNotOptArg, ResInt1=defaultNamedNotOptArg, ResInt2=defaultNamedNotOptArg
	# 		, ResByte=defaultNamedNotOptArg):
	# 	print("OnRxREPORTxH2")


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'Sincom.Machine.1'
class Machine(CoClassBaseClass): # A CoClass
	# Machine Class
	CLSID = IID('{EDF199C1-4F2E-11D3-9DC3-00A0249B4877}')
	coclass_sources = [
		_IMachineEvents,
	]
	default_source = _IMachineEvents
	coclass_interfaces = [
		IMachine,
	]
	default_interface = IMachine

IMachine_vtables_dispatch_ = 1
IMachine_vtables_ = [
	(( 'MachineID' , 'pVal' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MachineID' , 'pVal' , ), 1, (1, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MachineIP' , 'pVal' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MachineIP' , 'pVal' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MachinePort' , 'pVal' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MachinePort' , 'pVal' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MachineTimeout' , 'pVal' , ), 4, (4, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'MachineTimeout' , 'pVal' , ), 4, (4, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'HostID' , 'pVal' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'HostID' , 'pVal' , ), 5, (5, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'HostPort' , 'pVal' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'HostPort' , 'pVal' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'HostEnabled' , 'pVal' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'HostEnabled' , 'pVal' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'T_MACHINE_M' , 'OrderNum' , 'ret' , ), 10, (10, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'T_TPS_M' , 'OrderNum' , 'ret' , ), 11, (11, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'T_DATA_M' , 'OrderNum' , 'SFkt' , 'Name1' , 'Name2' , 
			 'ret' , ), 12, (12, (), [ (3, 1, None, None) , (3, 1, None, None) , (16392, 1, None, None) , 
			 (16392, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'T_VAR_M' , 'OrderNum' , 'VarMode' , 'VarSet' , 'VarDescr' , 
			 'ret' , ), 13, (13, (), [ (3, 1, None, None) , (3, 1, None, None) , (16392, 1, None, None) , 
			 (16392, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'R_NC4WPC_M' , 'OrderNum' , 'WPC' , 'NCProg' , 'DateVal' , 
			 'NCPLength' , 'ClampCubeSide' , 'TpFlag' , 'NCExtern' , 'ResInt1' , 
			 'ResInt2' , 'ResByte' , 'ret' , ), 14, (14, (), [ (3, 1, None, None) , 
			 (16392, 1, None, None) , (16392, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16392, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'R_REPORT_M' , 'OrderNum' , 'Typ' , 'Number' , 'ResInt1' , 
			 'ResInt2' , 'ResByte' , 'ret' , ), 15, (15, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16392, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'R_MESSAGE_M' , 'OrderNum' , 'Message' , 'ResInt1' , 'ResInt2' , 
			 'ResByte' , 'ret' , ), 16, (16, (), [ (3, 1, None, None) , (16392, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (16392, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'R_DATA_M' , 'OrderNum' , 'SFkt' , 'Name1' , 'Name2' , 
			 'Date' , 'LastFile' , 'ret' , ), 17, (17, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , (16392, 1, None, None) , (16392, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'R_VAR_M' , 'OrderNum' , 'VarMode' , 'VarSet' , 'VarDescr' , 
			 'VarData' , 'ret' , ), 18, (18, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			 (16392, 1, None, None) , (16392, 1, None, None) , (16392, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'R_DDEDATA_M' , 'OrderNum' , 'Application' , 'Topic' , 'Item' , 
			 'Data' , 'ret' , ), 19, (19, (), [ (3, 1, None, None) , (16392, 1, None, None) , 
			 (16392, 1, None, None) , (16392, 1, None, None) , (16392, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'C_DELETE_M' , 'OrderNum' , 'SFkt' , 'Name1' , 'Name2' , 
			 'ret' , ), 20, (20, (), [ (3, 1, None, None) , (3, 1, None, None) , (16392, 1, None, None) , 
			 (16392, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'C_MODE_M' , 'OrderNum' , 'Mode' , 'ret' , ), 21, (21, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'C_SYNCH_M' , 'OrderNum' , 'SynchFlag' , 'ret' , ), 22, (22, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'C_TPORDER_M' , 'OrderNum' , 'SDockPos' , 'DDockPos' , 'WPC' , 
			 'WPCTyp' , 'BufferFlag' , 'Priority' , 'ChainNum' , 'Vehicle' , 
			 'ResInt1' , 'ResInt2' , 'ResByte' , 'ret' , ), 23, (23, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16392, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (16392, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Shutdown_M' , ), 24, (24, (), [ ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'C_ORDER_M' , 'OrderNum' , 'SFkt' , 'Name1' , 'Name2' , 
			 'Name3' , 'Name4' , 'Parameter1' , 'Parameter2' , 'Parameter3' , 
			 'Parameter4' , 'ret' , ), 25, (25, (), [ (3, 1, None, None) , (3, 1, None, None) , 
			 (16392, 1, None, None) , (16392, 1, None, None) , (16392, 1, None, None) , (16392, 1, None, None) , (3, 1, None, None) , 
			 (3, 1, None, None) , (3, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'T_REPORT_M' , 'OrderNum' , 'ret' , ), 26, (26, (), [ (3, 1, None, None) , 
			 (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{EDF199C2-4F2E-11D3-9DC3-00A0249B4877}' : _IMachineEvents,
	'{EDF199C0-4F2E-11D3-9DC3-00A0249B4877}' : IMachine,
	'{EDF199C1-4F2E-11D3-9DC3-00A0249B4877}' : Machine,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{EDF199C0-4F2E-11D3-9DC3-00A0249B4877}' : 'IMachine',
}


NamesToIIDMap = {
	'_IMachineEvents' : '{EDF199C2-4F2E-11D3-9DC3-00A0249B4877}',
	'IMachine' : '{EDF199C0-4F2E-11D3-9DC3-00A0249B4877}',
}
