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
     menu2
     ;;
     "3")
     install_sb
     ;;
  esac
 }
 menu2()
 {
   clear
   echo "Choose Your SO:"
   echo "1 - Arch"
   echo "2 - Ubuntu"
   echo "3 - Return To The Menu"
   echo "Or  press enter to exit"
   read option;
   case $option in
   "1")
   install_arch
     ;;
    "2")
   install_ubuntu
     ;;
    "3")
   clear
   main
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
 install_arch()
 {
  clear && sudo pacman -S python && sudo pacman -S python-pip
 }
 install_ubuntu()
 {
  clear && sudo apt-get install nano && sudo apt-get install python && sudo apt-get install python3-pip
 }
 install_sb()
 {
   clear && pip3 install telepot --user && pip3 install PythonColorize --user && pip3 install urllib3 --user && pip3 install requests --user && pip3 install wikipedia --user
 }
main
