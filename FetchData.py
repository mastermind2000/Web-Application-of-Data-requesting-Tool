from math import sqrt
from obspy.taup import TauPyModel 
from obspy.core import UTCDateTime, read, Stream
import numpy as np
import sys
def DistDeg(sLon, sLat, eLon, eLat):
  return sqrt(pow((sLon - eLon),2) + pow(( sLat - eLat),2))

def CutData(Net, Stn, Loc, Chn, sLon, sLat, sElv, eLon, eLat, eDep, oY, oM, oD, oh, om, os, PreT, PosT, Arc):
  dist_deg = DistDeg(sLon=sLon, sLat=sLat, eLon=eLon, eLat=eLat)
  model = TauPyModel(model="iasp91")
  arr = model.get_travel_times(source_depth_in_km=eDep, distance_in_degree=dist_deg)
  FTT = arr[0].time
  OT = UTCDateTime(oY,oM,oD,oh,om,os)
  FAT =  OT + FTT
  t1 = FAT - PreT
  t2 = FAT + PosT
  sY = t1.strftime('%Y')
  sYMD = t1.strftime('%Y%m%d')
  wFile = Arc + '/'+Net+'/'+Stn +'/' + sY +'/'+ sYMD +'.' +Stn+'.'+Loc+'.'+Chn+'.mseed'
  st = read(wFile)
  return st.trim(t1,t2)

def CutDataManyStn(Arc,oDir, eId, sFile, eLon, eLat, eDep, oY, oM, oD, oh, om, os, PreT, PosT):
  Net_arr = np.loadtxt(sFile,dtype = 'str',comments = '#',delimiter = ',',usecols = [0])
  Net_arr = Net_arr.tolist()
  Stn_arr = np.loadtxt(sFile,dtype = 'str',comments = '#',delimiter = ',',usecols = [1])
  Stn_arr = Stn_arr.tolist()
  Loc_arr = np.loadtxt(sFile,dtype = 'str',comments = '#',delimiter = ',',usecols = [2])
  Loc_arr = Loc_arr.tolist()
  Chn_arr = np.loadtxt(sFile,dtype = 'str',comments = '#',delimiter = ',',usecols = [3])
  Chn_arr = Chn_arr.tolist()
  sLon_arr = np.loadtxt(sFile,comments = '#',delimiter = ',',usecols = [4])
  sLon_arr = sLon_arr.tolist()
  sLat_arr = np.loadtxt(sFile,comments = '#',delimiter = ',',usecols = [5])
  sLat_arr = sLat_arr.tolist()
  sElv_arr = np.loadtxt(sFile,comments = '#',delimiter = ',',usecols = [6])
  sElv_arr = sElv_arr.tolist()
  st = Stream(traces=None)
  for Net, Stn, Loc, Chn, sLon, sLat, sElv  in zip(Net_arr, Stn_arr, Loc_arr, Chn_arr, sLon_arr, sLat_arr, sElv_arr):
    st_tmp = CutData(Net=Net, Stn=Stn, Loc=Loc, Chn=Chn, sLon=sLon, sLat=sLat, sElv=sElv,
      eLon=eLon, eLat=eLat, eDep=eDep,
      oY=oY, oM=oM, oD=oD, oh=oh, om=om, os=os,
      PreT=PreT, PosT=PosT, Arc=Arc)
    st = st + st_tmp
    #break

  st.write(oDir+'/'+eId+'.mseed')

def CutDataManyEvt(PreT, PosT, oDir, Arc, sFile, eFile):
  with open(eFile, 'r') as fp:
    for eLine in fp:
      #print (eLine)
      if eLine[0] == '#':
	continue
      eId, oY, oM, oD, oh, om, os, eLat, eLon, eDep, Mag = eLine.strip().split(',')
      oY = int(oY); oM = int(oM); oD = int(oD); oh = int(oh); om = int(om); os = float(os)
      eLat = float(eLat); eLon = float(eLon); eDep = float(eDep); Mag = float(Mag)
      CutDataManyStn(Arc=Arc, oDir=oDir, eId=eId, sFile=sFile, eLon=eLon, eLat=eLat, eDep=eDep,   oY=oY, oM=oM, oD=oD, oh=oh, om=om, os=os, PreT=PreT, PosT=PosT)
      #print eId, oY+1, oM, oD, oh, om, os, eLat, eLon, eDep, Mag
      #break #eLine

if __name__ == '__main__':
	#PreT=5;PosT=100
	PreT = int(sys.argv[1])
	PosT = int(sys.argv[2])
	oDir='/var/www/html/Output'
	Arc='/var/www/html/archive'
	sFile ='/var/www/html/Input/Station.txt'
	eFile ='/var/www/html/Input/Catalog.txt'
	#sFile = sys.argv[3]
	#eFile = sys.argv[4]
 	CutDataManyEvt(PreT=PreT, PosT=PosT, oDir=oDir, Arc=Arc, sFile=sFile, eFile=eFile)

