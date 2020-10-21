# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:40:49 2020

@author: Eric.Englin
"""

def make_sign_df(input_file):
    from bs4 import BeautifulSoup
    import pandas as pd

    lat_list = []
    long_list = []
    img_file_name_list = []
    title_list  = []
    subject_list = []
    description_list = []
    tags_list = []
    time_stamp_list = []
    date_stamp_list = []
    elevation_list = []
    photo_direction_list = []
    make_list = []
    model_list = []
    district_list = []
    parkway_loc_list = []
    phys_loc_list = []
    mult_signs_list = []
    sign_type_list = []
    sign_condition_list = []
    main_req_list = []
    sign_material_list = []
    sign_face_list = []
    num_post_list = []
    post_material_list = []
    post_size_list = []
    sign_owner_list = []
    sign_text_list = []
    milepost_list = []
    reviewed_list = []
    inventory_number_list = []



    with open(input_file, 'r') as f:
        soup = BeautifulSoup(f, 'lxml')

      # After you have a soup object, you can access tags very easily.
      # For instance, you can iterate over and get <description> like so:

    #    for node in soup.select('Folder'):
    #
    #        print('done')
    #        x+=1
        for node in soup.select('Placemark'):
            for thing in node:
                if "longitude" in str(thing):
                    for subthing in thing:
                        if "longitude" in str(subthing):
                            temp = str(subthing)
                            long = (temp[temp.find(">")+1:temp.rfind("<")])
                        if "latitude" in str(subthing):
                            temp = str(subthing)
                            lat = temp[temp.find(">")+1:temp.rfind("<")]
                if "Sign Type" in str(thing):
                    for subthing in thing:
                        for subsubthing in subthing:
                            if "Original Photo" in str(subthing):
                                temp = str(subthing.get('href'))
                                img_file_name = temp
                            if "Title" in str(subsubthing):
                                temp = str(subsubthing)
                                title = (temp[temp.find("#003366")+9:-10])
                            if "Subject" in str(subsubthing):
                                temp = str(subsubthing)
                                subject = (temp[temp.find("#003366")+9:-10])
                            if "Comment" in str(subsubthing):
                                temp = str(subsubthing)
                                comment = (temp[temp.find("#003366")+9:-10])
                            if "Description" in str(subsubthing):
                                temp = str(subsubthing)
                                description = (temp[temp.find("#003366")+9:-10])
                            if "Tags" in str(subsubthing):
                                temp = str(subsubthing)
                                tags = (temp[temp.find("#003366")+9:-10])
                            if "Time Stamp" in str(subsubthing):
                                temp = str(subsubthing)
                                time_stamp = (temp[temp.find("#003366")+9:-10])
                            if "Date Stamp" in str(subsubthing):
                                temp = str(subsubthing)
                                date_stamp = (temp[temp.find("#003366")+9:-10])
                            if "Elevation" in str(subsubthing):
                                temp = str(subsubthing)
                                elevation = (temp[temp.find("#003366")+9:-10])
                            if "Photo Direction" in str(subsubthing):
                                temp = str(subsubthing)
                                photo_direction = (temp[temp.find("#003366")+9:-10])
                            if "Make" in str(subsubthing):
                                temp = str(subsubthing)
                                make = (temp[temp.find("#003366")+9:-10])
                            if "Model" in str(subsubthing):
                                temp = str(subsubthing)
                                model = (temp[temp.find("#003366")+9:-10])
                            if "District" in str(subsubthing):
                                temp = str(subsubthing)
                                district = (temp[temp.find("#003366")+9:-10])
                            if "Parkway Location" in str(subsubthing):
                                temp = str(subsubthing)
                                parkway_loc = (temp[temp.find("#003366")+9:-10])
                            if "Physical Location" in str(subsubthing):
                                temp = str(subsubthing)
                                phys_loc = (temp[temp.find("#003366")+9:-10])
                            if "Multiple Signs" in str(subsubthing):
                                temp = str(subsubthing)
                                mult_signs = (temp[temp.find("#003366")+9:-10])
                            if "Sign Type" in str(subsubthing):
                                temp = str(subsubthing)
                                sign_type = (temp[temp.find("#003366")+9:-10])
                            if "Sign Condition" in str(subsubthing):
                                temp = str(subsubthing)
                                sign_condition= (temp[temp.find("#003366")+9:-10])
                            if "Maintenance Required" in str(subsubthing):
                                temp = str(subsubthing)
                                main_req = (temp[temp.find("#003366")+9:-10])
                            if "Sign Material" in str(subsubthing):
                                temp = str(subsubthing)
                                sign_material= (temp[temp.find("#003366")+9:-10])
                            if "Sign Face" in str(subsubthing):
                                temp = str(subsubthing)
                                sign_face = (temp[temp.find("#003366")+9:-10])
                            if "Number of Posts" in str(subsubthing):
                                temp = str(subsubthing)
                                num_posts= (temp[temp.find("#003366")+9:-10])
                            if "Post Material" in str(subsubthing):
                                temp = str(subsubthing)
                                post_material= (temp[temp.find("#003366")+9:-10])
                            if "Post Size" in str(subsubthing):
                                temp = str(subsubthing)
                                post_size= (temp[temp.find("#003366")+9:-10])
                            if "Sign Owner" in str(subsubthing):
                                temp = str(subsubthing)
                                sign_owner = (temp[temp.find("#003366")+9:-10])
                            if "Sign Text" in str(subsubthing):
                                temp = str(subsubthing)
                                sign_text = (temp[temp.find("#003366")+9:-10])
                            if "Milepost" in str(subsubthing):
                                temp = str(subsubthing)
                                milepost = (temp[temp.find("#003366")+9:-10])
                            if "Reviewed" in str(subsubthing):
                                temp = str(subsubthing)
                                reviewed = (temp[temp.find("#003366")+9:-10])
                            if "Inventory Number" in str(subsubthing):
                                temp = str(subsubthing)
                                inventory_number = (temp[temp.find("#003366")+9:-10])


            if img_file_name in img_file_name_list:
                break #may also want to do a continue, depends if it copies the last file or not
            lat_list.append(lat)
            long_list.append(long)

            img_file_name_list.append(img_file_name)
            title_list.append(title)
            subject_list.append(subject)
            description_list.append(description)
            tags_list.append(tags)
            time_stamp_list.append(time_stamp)
            date_stamp_list.append(date_stamp)
            elevation_list.append(elevation)
            photo_direction_list.append(photo_direction)
            make_list.append(make)
            model_list.append(model)
            district_list.append(district)
            parkway_loc_list.append(parkway_loc)
            phys_loc_list.append(phys_loc)
            mult_signs_list.append(mult_signs)
            sign_type_list.append(sign_type)
            sign_condition_list.append(sign_condition)
            main_req_list.append(main_req)
            sign_material_list.append(sign_material)
            sign_face_list.append(sign_face)
            num_post_list.append(num_posts)
            post_material_list.append(post_material)
            post_size_list.append(post_size)
            sign_owner_list.append(sign_owner)
            sign_text_list.append(sign_text)
            milepost_list.append(milepost)
            reviewed_list.append(reviewed)
            inventory_number_list.append(inventory_number)

    map_df = pd.DataFrame({"Image File Name":img_file_name_list,
                           'LON':long_list,
                          'LAT':lat_list,
                          "Title":title_list,
                          "Subject":subject_list,
                          "Description":description_list,
                          "Tags":tags_list,
                          "Time Stamp":time_stamp_list,
                          "Date Stamp":date_stamp_list,
                          "Elevation":elevation_list,
                          "Photo Direction":photo_direction_list,
                          "Make":make_list,
                          "Model":model_list,
                           "District":   district_list,
                          "Parkway Location":parkway_loc_list,
                          "Physical Location":phys_loc_list,
                          'Multiple Signs': mult_signs_list,
                          'Sign Type':sign_type_list,
                           "Sign Condition": sign_condition_list,
                           "Maintenance Required": main_req_list,
                           "Sign Material": sign_material_list,
                           "Sign Face": sign_face_list ,
                           "Number of posts": num_post_list,
                           "Post Material": post_material_list,
                           "Post Size": post_size_list,
                          'Sign Owner':sign_owner_list,
                          "Sign Text":sign_text_list,
                          "Milepost":milepost_list,
                          "Reviewed":reviewed_list,
                          "Inventory Number":inventory_number_list
                          })
    map_df['LON']=map_df['LON'].astype(float)
    map_df['LAT']=map_df['LAT'].astype(float)

    return map_df

def map_points(map_df, filename):
    import folium
    import numpy as np

    locations = map_df[['LAT', 'LON']]
    locationlist = locations.values.tolist()
    map_df = map_df.reset_index()

    map1 = folium.Map(location=[np.mean(map_df.LAT), np.mean(map_df.LON)], zoom_start=7,
                     tiles = 'Stamen Terrain')
    for point in range(0, len(locationlist)):
        folium.Marker(locationlist[point], popup=('Sign Type: ' + map_df['Image File Name'][point])).add_to(map1)

    filename = filename + ".html"
    map1.save(filename)
    return map1
