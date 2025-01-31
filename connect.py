import openstack
conn = openstack.connect(cloud_name='openstack')



IMAGE = 'ubuntu-16.04-x86_64'
FLAVOUR = 'c1.c1r1'
NETWORK = 'private-net'
KEYPAIR = 'dackja1-key'

image = conn.compute.find_image(IMAGE)
flavour = conn.compute.find_flavor(FLAVOUR)
network = conn.network.find_network(NETWORK)
keypair = conn.compute.find_keypair(KEYPAIR)


SERVER = 'dackja1-server'
server = conn.compute.create_server(
name=SERVER, image_id=image.id, flavor_id=flavour.id,
networks=[{"uuid": network.id}], key_name=keypair.name)

server = conn.compute.wait_for_server(server)

public_net = conn.network.find_network('public-net')
floating_ip = conn.network.create_ip(floating_network_id=public_net.id)

conn.compute.add_floating_ip_to_server(server, floating_ip.floating_ip_address)


for server in conn.compute.servers():
    print (server)

