Running
========

Local test run
--------------

::

    mkdir results

    xAH_run.py --files EoverPAnalysis/filelists/data15_13TeV_lowmu_test1.txt --inputList --config EoverPAnalysis/scripts/config_eop_data_lowmu.py --submitDir results/eop_data_test_0 --verbose --force direct

First condor test run
---------------------

::

    source EoverPAnalysis/scripts/run_condor_test_eop_lowmu.sh 0 # where '0' is a tag for the run

.. note::
    The output will then be located in 'results', e.g. 
    results/condor_test_eop_lowmu_{mc,data}_YYYYMMDD_0/

The condor output histograms and cutflows can easily be merged, just run (after condor has finished)

::
    
    source $ROOTCOREBIN/../EoverPAnalysis/scripts/merge_condor_eop.py $ROOTCOREBIN/../results/run_condor_eop_lowmu_latest.log