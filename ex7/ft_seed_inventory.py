#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_seed_inventory.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/15 21:20:24 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/15 21:20:24 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    print(f"{seed_type.capitalize()} seeds:", end=" ")
    match unit:
        case x if "packets" == x:
            print(f"{quantity} packets available")
        case x if "grams" == x:
            print(f"{quantity} grams total")
        case x if "area" == x:
            print(f"covers {quantity} square meters")
        case _:
            print("Unknown unit type")
