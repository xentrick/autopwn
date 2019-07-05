#
# Cookbook:: metasploitable
# Recipe:: chatbot
#
# Copyright:: 2017, Rapid7, All Rights Reserved.
#
#

include_recipe 'metasploitable::ruby23'
include_recipe 'metasploitable::nodejs'

package 'unzip'

bash "Install dependencies" do
  code <<-EOH
    npm install express
    npm install cors
  EOH
end

cookbook_file '/tmp/chatbot.zip' do
  source 'chatbot/chatbot.zip'
  mode '0700'
end

execute 'unzip chatbot' do
  command 'unzip /tmp/chatbot.zip -d /opt'
end

execute 'chown chatbot' do
  command "chown -R root:root /opt/chatbot"
end

execute 'chmod chatbot' do
  command 'chmod -R 700 /opt/chatbot'
end

execute 'install chatbot' do
  command '/opt/chatbot/install.sh'
end

service 'chatbot' do
  supports restart: false, start: true, reload: false, status: false
  action [:enable, :start]
end
