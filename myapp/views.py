from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Image

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

import os

def index(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)

def process_view(request):
    G = nx.Graph()
    all_points = {}

    def add_nodes(pt_dict):
        for pt in pt_dict:
            G.add_node(pt)
            all_points[pt] = pt_dict[pt]
            
    def add_edge(pt1,pt2):
        coord1 = all_points[pt1]
        coord2 = all_points[pt2]
        G.add_edge(pt1,pt2,weight=int(np.sqrt((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2)))

    def add_edges(pt_dict):
        temp = list(pt_dict)
        for i in range(len(temp)-1):
            G.add_edge(temp[i],temp[i+1],weight=pt_dict[temp[i+1]][0]-pt_dict[temp[i]][0])

    top_dict = {
    '6401': (65,82),
    '6403': (102,82),
    '6404': (140,82),
    '6405': (147,82),
    '6407': (198,82),
    '6409': (270,82),
    '6411': (298,82),
    '6413': (373,82),
    '6406': (387,82),
    '6415': (404,82),
    '6419': (530,82),
    '6410': (550,82),
    '6421': (560,82),
    '6412': (580,82),
    '6423': (630,82),
    '6414': (650,82),
    '6425': (668,82),
    '6416': (725,82),
    '6427': (733,82),
    '6429': (763,82)
    }

    add_nodes(top_dict)
    add_edges(top_dict)

    mid_dict = {
        'ch_bot': (470,670),
        'ch_elev': (470,526),
        'ch_mid': (470,453),
        '6504': (470,417),
        '6508': (470,317),
        '6408': (470,163),
        'ch_top': (470,82)
    }

    add_nodes(mid_dict)
    add_edges(mid_dict)
    add_edge('ch_top','6415')
    add_edge('ch_top','6419')

    elev_dict = {
        'men_br': (508,526),
        'elev_ctrtop': (573,526),
        'women_br': (639,526),
        'elev': (573,606),
        'elev_bot': (573,670)
    }

    add_nodes(elev_dict)
    add_edge('men_br','elev_ctrtop')
    add_edge('women_br','elev_ctrtop')
    add_edge('elev','elev_ctrtop')
    add_edge('elev','elev_bot')
    add_edge('ch_elev','men_br')
    add_edge('ch_bot','elev_bot')

    left_dict = {
        '6329': (102,117),
        '6323': (102,304),
        '6507': (102,316),
        '6503': (102, 416),
        'left_mid': (102,453),
        '6317': (102,527),
        '6312': (102,552),
        '6313': (91,581),
        '6311': (91,610),
        '6309': (91,680),
        '6307': (91,710),
        '6305': (91,764)
    }

    add_nodes(left_dict)
    add_edges(left_dict)
    add_edge('6403','6329')

    leftmid_dict = {
        '6512': (212,453),
        '6514': (244,453),
        'left_alley': (286,453),
        '6516': (361,453)
    }

    add_nodes(leftmid_dict)
    add_edges(leftmid_dict)
    add_edge('left_mid','6512')
    add_edge('6516','ch_mid')

    leftalley_dict = {
        '6501': (286,381),
        '6502': (286,381),
        '6505': (286,349),
        '6506': (286,349),
        '6509': (286,284),
        '6510': (286,284),
        '6511': (286,284)
    }

    add_nodes(leftalley_dict)
    add_edges(leftalley_dict)
    add_edge('left_alley','6501')

    botleft_dict = {
        '6215': (40,819),
        '6213': (91,819),
        '6211': (143,819),
        '6209': (171,819),
        '6207': (246,819),
        '6205': (275,819),
        '6203': (300,819)
    }

    add_nodes(botleft_dict)
    add_edges(botleft_dict)
    add_edge('6305','6213')

    botL_dict = {
        '6148': (300,670),
        '6150': (300,670),
        '6146': (400,670)
    }

    add_nodes(botL_dict)
    add_edges(botL_dict)
    # add_edge('6203','6143')
    add_edge('6203','6148')
    # add_edge('6145','ch_bot')
    add_edge('6146','ch_bot')

    right_dict = {
        '6101': (840,155),
        '6104': (840,181),
        '6103': (840,185),
        '6105': (840,259),
        '6106': (840,286),
        '6107': (840,288),
        '6108': (840,316),
        '6109': (840,362),
        '6111': (840,390),
        '6113': (840,465),
        '6110': (840,488),
        '6115': (840,526)
    }

    add_nodes(right_dict)
    add_edges(right_dict)
    add_edge('6429','6101')
    add_edge('women_br','6115')

    G.add_node('6135')
    all_points['6135'] = (573,720)
    add_edge('elev_bot','6135')

    G.add_node('6137')
    all_points['6137'] = (573,754)
    add_edge('6137','6135')

    G.add_node('6139')
    all_points['6139'] = (522,754)
    add_edge('6137','6139')

    G.add_node('6145')
    all_points['6145'] = (442,754)
    add_edge('6145','6139')

    G.add_node('6141')
    all_points['6141'] = (433,754)
    add_edge('6145','6141')

    G.add_node('6143')
    all_points['6143'] = (399,754)
    add_edge('6143','6141')

    G.add_node('6133')
    all_points['6133'] = (623,754)
    add_edge('6133','6137')

    G.add_node('6131')
    all_points['6131'] = (700,720)
    add_edge('6131','6135')

    G.add_node('6116')
    all_points['6116'] = (737,720)
    add_edge('6131','6116')

    G.add_node('6129')
    all_points['6129'] = (750,720)
    add_edge('6116','6129')

    G.add_node('6127')
    all_points['6127'] = (795,720)
    add_edge('6127','6129')

    G.add_node('6125')
    all_points['6125'] = (778,682)
    add_edge('6125','6129')

    G.add_node('6119')
    all_points['6119'] = (836,598)
    add_edge('6125','6119')

    G.add_node('6117')
    all_points['6117'] = (836,569)
    add_edge('6117','6119')

    def plot_points(pt_dict):
        for pt in pt_dict:
            if pt=='6503' or pt=='6507': # for some reason, these inner rooms are odd
                plt.plot(pt_dict[pt][0],pt_dict[pt][1],'ob',markersize=8)
            elif pt.isdigit() and int(pt)%2 == 0: # inner rooms are all even
                plt.plot(pt_dict[pt][0],pt_dict[pt][1],'ob',markersize=8)
            elif pt.isdigit():
                plt.plot(pt_dict[pt][0],pt_dict[pt][1],'og',markersize=8)
            else:
                plt.plot(pt_dict[pt][0],pt_dict[pt][1],'oy',markersize=10)
    
    plt.rcParams['figure.figsize'] = [20, 10]

    if request.method == 'GET':
        input1 = request.GET.get('room', '')
        output_file = 'data.txt'
        with open(output_file, 'w') as file:
            file.write(input1)
    if request.method == 'POST':
        input_file = 'data.txt' 
        with open(input_file, 'r') as file:
            input1 = file.readline()
        if input1 == '':
            input1 = request.POST.get('input1') # src
        # input1 = request.POST.get('input1') # src
        input2 = request.POST.get('input2') # dest

        path = nx.shortest_path(G,input1,input2)
        
        img = mpimg.imread('/Users/kevin/Documents/mapweb/myproject/static/floor6_map.png')

        plt.annotate('YOU ARE HERE',all_points[path[0]])
        plt.plot(all_points[path[0]][0],all_points[path[0]][1],'Dy',markersize=15)

        # star the destination
        plt.plot(all_points[path[-1]][0],all_points[path[-1]][1],'*y',markersize=25)

        for i in range(len(path)-1):
            pt1 = all_points[path[i]]
            pt2 = all_points[path[i+1]]
            plt.plot((pt1[0],pt2[0]),(pt1[1],pt2[1]),'r',linewidth=5,linestyle='-')

        imgplot = plt.imshow(img)
        my_path = str(os.path.abspath(__file__))
        if my_path.endswith('/myapp/views.py'):
            my_path = my_path[:-15]
        plt.savefig(my_path + '/static/output.png', bbox_inches='tight')
        # plt.savefig('/Users/kevin/Documents/mapweb/myproject/static/output.png', bbox_inches='tight')
        # Process the input strings and generate the output image
        # output_image = process_inputs(input1, input2)

        return render(request, 'output.html')
    # return render(request, 'output.html', {'output_image': output_image})
    # return redirect('output.html')
    # template = loader.get_template('output.html')
    # return HttpResponse(template.render())

    return render(request, 'input.html')

def process_inputs(input1, input2):
    # Your code to process the input strings and generate the output image
    # ...

    # Return the path or URL to the output image file
    # return 'floor6_map.png'
    return
