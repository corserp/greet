# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'slayer/goku'

Gem::Specification.new do |spec|
  spec.name          = "slayer"
  spec.version       = Slayer::VERSION
  spec.authors       = ["sean"]
  spec.email         = ["seanathomas1@outlook.com"]
  spec.description   = %q{igoku}
  spec.summary       = %q{igokury}
  spec.homepage      = ""
  spec.license       = "MIT"

  spec.files         = `git ls-files`.split($/)
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.test_files    = spec.files.grep(%r{^(test|spec|features)/})
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.3"
  spec.add_development_dependency "rake"
end
