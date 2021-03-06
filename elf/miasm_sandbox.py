import logging
from pdb import pm
from miasm.analysis.sandbox import Sandbox_Linux_x86_64
from miasm.jitter.jitload import log_func

# Insert here user defined methods

# Parse arguments
parser = Sandbox_Linux_x86_64.parser(description="ELF sandboxer")
parser.add_argument("filename", help="ELF Filename")
options = parser.parse_args()

# Create sandbox
sb = Sandbox_Linux_x86_64(options.filename, options, globals())

log_func.setLevel(logging.ERROR)

# Run
sb.run()

assert(sb.jitter.run is False)
