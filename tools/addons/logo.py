"""This module provides a function that prints the logo's application."""

import os

from colorama import Fore as F


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
    logo = """
░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░ 
"""
    print(f"{F.RED}{logo}")
    print("├─── BICP DDOS")
    print("├─── : HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
    if os.name != "nt":
        print("├─── : SYN-FLOOD")
        print("├─── : ARP-SPOOF | DISCONNECT")
    print("├───┐")
