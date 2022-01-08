import telnetlib

HOST = "localhost"
PORT = 3636
timeout = 100

with telnetlib.Telnet(HOST, PORT, timeout) as session:
    session.write(b"lock\n")
    session.write(b"setmode:ambilight\n")
    session.write(b"unlock\n")
    session.write(b"exit\n")

