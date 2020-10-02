def generate_melon_delivery_report(file_loc, day):

    the_file = open(file_loc)
    print(day)

    for line in the_file:
        if "|" in line:
            line = line.rstrip()
            words = line.split('|')

            melon = words[0]
            count = words[1]
            amount = words[2]
            #print(words)

            print("Delivered {} {}s for total of ${}".format(count, melon, amount))
  
    the_file.close()


print(generate_melon_delivery_report("um-deliveries-20140519.txt", "Day 1"))
print(generate_melon_delivery_report("um-deliveries-20140520.txt", "Day 2"))
print(generate_melon_delivery_report("um-deliveries-20140521.txt", "Day 3"))