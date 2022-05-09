output "instance_ip_addr" {
  value = aws_instance.my_server.public_ip
}