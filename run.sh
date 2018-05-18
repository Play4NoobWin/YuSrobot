#!/bin/bash
clear
echo " **    **          ********                 **                 **  
//**  **          **//////                 /**                /**  
 //****   **   **/**        ******  ****** /**       ******  ******
  //**   /**  /**/*********//**//* **////**/******  **////**///**/ 
   /**   /**  /**////////** /** / /**   /**/**///**/**   /**  /**  
   /**   /**  /**       /** /**   /**   /**/**  /**/**   /**  /**  
   /**   //****** ******** /***   //****** /****** //******   //** 
   //     ////// ////////  ///     //////  /////    //////     // " 


main()
  {
    echo "Choose an option:"
    echo "1 - Start Bot"    
    echo "2 - Install System Requeriments"
    echo "3 - Install Bot Requeriments"
    echo "Or press enter to exit"
    read option;
    case $option in
    "1")
     run_bot
     ;;
    "2")
     install_sr
     ;;
     "3")
     install_sb
     ;;
  esac
 }
 run_bot()
 {
   for file in *
   do
   python3 main.py
   done
 }
 install_sr()
 {
   sudo apt-get install nano && sudo apt-get install python && sudo apt-get install python3-pip
   for file in *
   do
   sh run.sh
   done
 }
 install_sb()
 {
   pip3 install telepot && pip3 install PythonColorize
   for file in *
   do
   sh run.sh
   done
 }
main