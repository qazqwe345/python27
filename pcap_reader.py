import dpkt
import socket
 
#----------------------------------------------------------------------
def printPcap(pcap):
    """"""
    for(ts,buf) in pcap:
        try:
            eth=dpkt.ethernet.Ethernet(buf);
            ip=eth.data;
            src=socket.inet_ntoa(ip.src);
            dst=socket.inet_ntoa(ip.dst);
            tcp=ip.data;#tcp.dport  tcp.sport
            print '[+]Src: '+src+ ' --->Dst: '+ dst
        except:
            pass;
#----------------------------------------------------------------------
def main():
    """"""
    f=open('test.pcap');#1.open file
    pcap=dpkt.pcap.Reader(f);# init pcap obj
    printPcap(pcap);
 
if __name__ == '__main__':
    main();
