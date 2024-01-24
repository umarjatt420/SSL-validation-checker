import ssl
import socket

def SSL_info(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                issue_date = cert['notBefore']
                expiry_date = cert['notAfter']
                return issue_date, expiry_date
    except(socket.error, ssl.SSLError, ConnectionError) as e:
        return None, None
        
if __name__ == "__main__":
    domain = input("Enter the domain (e.g., https://www.example.com/): ")
    issue_date, expiry_date = SSL_info(domain)
 
if issue_date and expiry_date:
    print(f"SSL Certificate Information for {domain}:")
    print(f"Issue Date: {issue_date}")
    print(f"Expiry Date: {expiry_date}")
else:
    print(f"Unable to retrieve SSL certificate information for {domain}.",
     f"Please check the domain name or make sure it uses SSL (HTTPS).")