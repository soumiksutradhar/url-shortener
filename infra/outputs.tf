output "aws_instance_public_ip"{
	value = aws_instance.d03_server.public_ip
	description = "Public IP of d03_server EC2 instance"
}
