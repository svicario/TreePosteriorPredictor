PhyloPPTester
=============

Perform a Posterior Predictive test to validate phylogenetic inference done with MrBayes and ExaBayes

The project includes the following files:

* jsonify.py -- it transform the the output from mrBayes or Exabayes in a json format
* PosteriorSimulator.py -- it parse the json file and use evolver from PAML package to simulate new data set, then each data partition of each data set is scored using the maximum likelihood statistics. An XML that describe the difference between observed and simulated data is given in standardouput
* evolver -- software compiled for macosx 10.9.2. details in README_PAML
* README_PAML -- all details for the distribution of PAML suite and the included evolver software
* Folder with protein model in PAML format
* README.md -- this file

## Dependency
The project need the evolver program see README_PAML for details on this software
The project was written in Python 2.7. backward compatibility but should span from 2.4 and on, but was not tested
The following module were used:

* [BioPython 1.60](http://biopython.org/)
* [Numpy 1.8](http://www.numpy.org/)

##Jsonify
There are 6 inputs that need to be passed using the unix cmd line style
here the details:

    -j jsonoutput
    -i nexus input
    -p prefix
    -b burnin
    -s sample size 
    -m boolean 0 or 1 the input is mrbayes (otherwise exabayes)   
###Limitation of Jsonify
The program correctly represent partitioned model in which one type of data (DNA, Protein or Codon) is present in the multiple sequences alignment (MSA). MSA with mixed type may not correctly represented.

At the moment protein model with fixed parameters are represented with a common name in the field "shape" within the "matrix" section. Future version will spell out actual value of all parameters to avoid name ambiguity

The program do not represent model with parameters changing value across the tree

##PosteriorSimulator
There are the following options:

    -j jsoninput path
    -e path to  evolver
    -i input MSA
    -f input MSA format (all format accepted by biopython)

##Example of use 
__MrBayes example__

    cd example/mrbayes
    python  ../../Jsonify.py -j prova.json -i Limenitidinae6.nex -p Limenitidinae6.nex -b 0 -s 100 -m 1
    python ../../PosteriorSimulator.py -s prova.json -i Limenitidinae6.nex -f nexus

__ExaBayes example__

   cd example/exabayes
   python ../../Jsonify.py   -j prova.json -i config.nex -p ExaBayes -b 10 -m 0 -s 10
   python ../../PosteriorSimulator.py  -s prova.json -i aln.phy -f phylip


  
