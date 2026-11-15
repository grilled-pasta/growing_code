# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: alkonsta <alkonsta@student.codam.nl>      +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/11/15 11:06:16 by alkonsta         #+#    #+#              #
#    Updated: 2026/11/15 11:10:23 by alkonsta        ###   ########.nl        #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total() -> None:
    sum, i = 0, 1
    while i <= 3:
        sum += int(input(f"Day {i} harvest: "))
        i += 1
    print(f"Total harvest: {sum}")
