import mirror_engine
import log
logger = log.make_logger("log")
logger.info("Starting.")
engine = mirror_engine.MirrorEngine()
engine.initialize()
while True:
	try:
		engine.update()
		engine.run()
	except Exception as e:
		logger.exception(f"Uncaught exception! {e}")

# TODO:
# compare diffs on up and downstream
# update downstream dme with upstream
