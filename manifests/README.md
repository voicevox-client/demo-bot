# demo's manifests

## Add secret
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: bot-secret
type: Opaque
data:
  token: (discord token's base64)
```

## Apply
```sh
kubectl apply -f manifests
```
