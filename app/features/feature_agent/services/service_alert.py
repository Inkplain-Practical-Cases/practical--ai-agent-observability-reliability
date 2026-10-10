# Alert service evaluates aggregate failure rate using a minimum sample floor.
def service_alert(total:int,failures:int,threshold:float=0.2):
    if not 0<=failures<=total: raise ValueError('invalid counts')
    if total<10: return {'alert':False,'reason':'insufficient_samples'}
    alert=failures/total>=threshold
    return {'alert':alert,'reason':'high_error_rate' if alert else 'healthy'}
